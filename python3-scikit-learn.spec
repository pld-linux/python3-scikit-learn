# TODO:
# - system libs:
#   - libsvm, liblinear
#   - python modules in externals: _arff _lobpcg _pep562 _pilutil _scipy_linalg six
# - test failures (a few with python2, cannot run with python3)
#
# Conditional build:
%bcond_with	tests	# unit tests (some failing as of 0.22.2)

%define	joblib_ver	0.11
%define	numpy_ver	1.8.2
%define	scipy_ver	0.13.3

Summary:	Set of Python 3 modules for machine learning and data mining
Summary(pl.UTF-8):	Zbiór modułów Pythona 3 do uczenia maszynowego i eksporacji danych
Name:		python3-scikit-learn
Version:	1.6.1
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/scikit-learn/
Source0:	https://files.pythonhosted.org/packages/source/s/scikit-learn/scikit_learn-%{version}.tar.gz
# Source0-md5:	f7e65a9e011c8ec6d0eb4dbe32edcbdc
URL:		https://scikit-learn.org/
BuildRequires:	findutils
BuildRequires:	libgomp-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python3-Cython
BuildRequires:	python3-build
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-installer
BuildRequires:	python3-numpy-devel >= %{numpy_ver}
BuildRequires:	python3-scipy >= %{scipy_ver}
%if %{with tests}
BuildRequires:	python3-joblib >= %{joblib_ver}
BuildRequires:	python3-pytest >= 3.3.0
%endif
Requires:	python3-joblib >= %{joblib_ver}
Requires:	python3-modules >= 1:3.5
Requires:	python3-numpy >= %{numpy_ver}
Requires:	python3-scipy >= %{scipy_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

%description -l pl.UTF-8
scikit-learn to moduł Pythona do uczenia maszynowego, zbudowany w
oparciu o SciPy i rozprowadzany na 3-punktowej licencji BSD.

%prep
%setup -q -n scikit_learn-%{version}

%build
%py3_build_pyproject

%if %{with tests}
cp -pr sklearn/datasets/{data,descr,images} build-3/lib.*/sklearn/datasets
cp -pr sklearn/datasets/tests/data build-3/lib.*/sklearn/datasets/tests
cd build-3/lib.*
PYTHONPATH=$(pwd) \
%{__python3} -m pytest sklearn
%{__rm} -r sklearn/datasets/{data,descr,images} sklearn/datasets/tests/data
cd ../..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/sklearn/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/sklearn/{cluster,compose,covariance,cross_decomposition,datasets,decomposition,ensemble,ensemble/_hist_gradient_boosting,experimental,feature_extraction,feature_selection,frozen,gaussian_process,impute,inspection,linear_model,_loss,manifold,metrics,metrics/{_plot,cluster},mixture,model_selection,neighbors,neural_network,preprocessing,semi_supervised,svm,tree,utils}/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/sklearn/cluster/_hdbscan/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/sklearn/utils/_test_common

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/sklearn/{svm,utils}/src

find $RPM_BUILD_ROOT%{py3_sitedir}/sklearn/ -type f -name '*.pyx*' -delete
find $RPM_BUILD_ROOT%{py3_sitedir}/sklearn/ -type f -name '*.pxd*' -delete
find $RPM_BUILD_ROOT%{py3_sitedir}/sklearn/ -type f -name '*.pxi*' -delete
find $RPM_BUILD_ROOT%{py3_sitedir}/sklearn/ -type f -name 'meson.build' -delete

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README.rst
%dir %{py3_sitedir}/sklearn
%attr(755,root,root) %{py3_sitedir}/sklearn/_isotonic.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/*.py
%attr(755,root,root) %{py3_sitedir}/sklearn/__pycache__
%dir %{py3_sitedir}/sklearn/__check_build
%attr(755,root,root) %{py3_sitedir}/sklearn/__check_build/_check_build.cpython-*.so
%{py3_sitedir}/sklearn/__check_build/*.py
%{py3_sitedir}/sklearn/__check_build/__pycache__
%{py3_sitedir}/sklearn/_build_utils
%dir %{py3_sitedir}/sklearn/_loss
%{py3_sitedir}/sklearn/_loss/*.py
%{py3_sitedir}/sklearn/_loss/__pycache__
%attr(755,root,root) %{py3_sitedir}/sklearn/_loss/_loss.*.so
%dir %{py3_sitedir}/sklearn/cluster
%attr(755,root,root) %{py3_sitedir}/sklearn/cluster/_dbscan_inner.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/cluster/_hierarchical_fast.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/cluster/_k_means*.cpython-*.so
%{py3_sitedir}/sklearn/cluster/*.py
%{py3_sitedir}/sklearn/cluster/__pycache__
%dir %{py3_sitedir}/sklearn/cluster/_hdbscan
%attr(755,root,root) %{py3_sitedir}/sklearn/cluster/_hdbscan/_linkage.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/cluster/_hdbscan/_reachability.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/cluster/_hdbscan/_tree.cpython-*.so
%{py3_sitedir}/sklearn/cluster/_hdbscan/*.py
%{py3_sitedir}/sklearn/cluster/_hdbscan/__pycache__
%{py3_sitedir}/sklearn/compose
%{py3_sitedir}/sklearn/covariance
%{py3_sitedir}/sklearn/cross_decomposition
%dir %{py3_sitedir}/sklearn/datasets
%attr(755,root,root) %{py3_sitedir}/sklearn/datasets/_svmlight_format_fast.cpython-*.so
%{py3_sitedir}/sklearn/datasets/*.py
%{py3_sitedir}/sklearn/datasets/__pycache__
%{py3_sitedir}/sklearn/datasets/data
%{py3_sitedir}/sklearn/datasets/descr
%{py3_sitedir}/sklearn/datasets/images
%dir %{py3_sitedir}/sklearn/decomposition
%attr(755,root,root) %{py3_sitedir}/sklearn/decomposition/_cdnmf_fast.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/decomposition/_online_lda_fast.cpython-*.so
%{py3_sitedir}/sklearn/decomposition/*.py
%{py3_sitedir}/sklearn/decomposition/__pycache__
%dir %{py3_sitedir}/sklearn/ensemble
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_gradient_boosting.cpython-*.so
%{py3_sitedir}/sklearn/ensemble/*.py
%{py3_sitedir}/sklearn/ensemble/__pycache__
%dir %{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/_binning.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/_bitset.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/_gradient_boosting.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/_predictor.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/common.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/histogram.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/splitting.cpython-*.so
%{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/*.py
%{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/__pycache__
%{py3_sitedir}/sklearn/experimental
%dir %{py3_sitedir}/sklearn/externals
%{py3_sitedir}/sklearn/externals/*.py
%{py3_sitedir}/sklearn/externals/__pycache__
%{py3_sitedir}/sklearn/externals/_packaging
%{py3_sitedir}/sklearn/externals/_scipy
%dir %{py3_sitedir}/sklearn/feature_extraction
%attr(755,root,root) %{py3_sitedir}/sklearn/feature_extraction/_hashing_fast.cpython-*.so
%{py3_sitedir}/sklearn/feature_extraction/*.py
%{py3_sitedir}/sklearn/feature_extraction/__pycache__
%{py3_sitedir}/sklearn/feature_selection
%{py3_sitedir}/sklearn/frozen
%{py3_sitedir}/sklearn/gaussian_process
%{py3_sitedir}/sklearn/impute
%{py3_sitedir}/sklearn/inspection
%dir %{py3_sitedir}/sklearn/linear_model
%attr(755,root,root) %{py3_sitedir}/sklearn/linear_model/_cd_fast.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/linear_model/_sag_fast.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/linear_model/_sgd_fast.cpython-*.so
%{py3_sitedir}/sklearn/linear_model/*.py
%{py3_sitedir}/sklearn/linear_model/__pycache__
%{py3_sitedir}/sklearn/linear_model/_glm
%dir %{py3_sitedir}/sklearn/manifold
%attr(755,root,root) %{py3_sitedir}/sklearn/manifold/_barnes_hut_tsne.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/manifold/_utils.cpython-*.so
%{py3_sitedir}/sklearn/manifold/*.py
%{py3_sitedir}/sklearn/manifold/__pycache__
%dir %{py3_sitedir}/sklearn/metrics
%attr(755,root,root) %{py3_sitedir}/sklearn/metrics/_dist_metrics.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/metrics/_pairwise_fast.cpython-*.so
%{py3_sitedir}/sklearn/metrics/*.py
%{py3_sitedir}/sklearn/metrics/__pycache__
%{py3_sitedir}/sklearn/metrics/_plot
%dir %{py3_sitedir}/sklearn/metrics/cluster
%attr(755,root,root) %{py3_sitedir}/sklearn/metrics/cluster/_expected_mutual_info_fast.cpython-*.so
%{py3_sitedir}/sklearn/metrics/cluster/*.py
%{py3_sitedir}/sklearn/metrics/cluster/__pycache__
%dir %{py3_sitedir}/sklearn/metrics/_pairwise_distances_reduction
%{py3_sitedir}/sklearn/metrics/_pairwise_distances_reduction/*.py
%{py3_sitedir}/sklearn/metrics/_pairwise_distances_reduction/__pycache__
%attr(755,root,root) %{py3_sitedir}/sklearn/metrics/_pairwise_distances_reduction/*cpython-*.so
%{py3_sitedir}/sklearn/mixture
%{py3_sitedir}/sklearn/model_selection
%dir %{py3_sitedir}/sklearn/neighbors
%attr(755,root,root) %{py3_sitedir}/sklearn/neighbors/_ball_tree.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/neighbors/_kd_tree.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/neighbors/_partition_nodes.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/neighbors/_quad_tree.cpython-*.so
%{py3_sitedir}/sklearn/neighbors/*.py
%{py3_sitedir}/sklearn/neighbors/__pycache__
%{py3_sitedir}/sklearn/neural_network
%dir %{py3_sitedir}/sklearn/preprocessing
%attr(755,root,root) %{py3_sitedir}/sklearn/preprocessing/_csr_polynomial_expansion.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/preprocessing/_target_encoder_fast.cpython-*.so
%{py3_sitedir}/sklearn/preprocessing/*.py
%{py3_sitedir}/sklearn/preprocessing/__pycache__
%{py3_sitedir}/sklearn/semi_supervised
%dir %{py3_sitedir}/sklearn/svm
%attr(755,root,root) %{py3_sitedir}/sklearn/svm/_liblinear.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/svm/_libsvm.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/svm/_libsvm_sparse.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/svm/_newrand.cpython-*.so
%{py3_sitedir}/sklearn/svm/*.py
%{py3_sitedir}/sklearn/svm/__pycache__
%dir %{py3_sitedir}/sklearn/tree
%attr(755,root,root) %{py3_sitedir}/sklearn/tree/_criterion.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/tree/_partitioner.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/tree/_splitter.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/tree/_tree.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/tree/_utils.cpython-*.so
%{py3_sitedir}/sklearn/tree/*.py
%{py3_sitedir}/sklearn/tree/__pycache__
%dir %{py3_sitedir}/sklearn/utils
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_cython_blas.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_fast_dict.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_heap.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_isfinite.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_openmp_helpers.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_random.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_seq_dataset.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_sorting.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_typedefs.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_vector_sentinel.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_weight_vector.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/arrayfuncs.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/murmurhash.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/sparsefuncs_fast.cpython-*.so
%{py3_sitedir}/sklearn/utils/*.py
%{py3_sitedir}/sklearn/utils/__pycache__
%{py3_sitedir}/sklearn/utils/_estimator_html_repr.css
%{py3_sitedir}/scikit_learn-%{version}.dist-info
