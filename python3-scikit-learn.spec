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
Version:	0.22.2.post1
Release:	6
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/scikit-learn/
Source0:	https://files.pythonhosted.org/packages/source/s/scikit-learn/scikit-learn-%{version}.tar.gz
# Source0-md5:	4c8d2ab712bd03e01bc55291e1f7bc6e
URL:		https://scikit-learn.org/
BuildRequires:	libgomp-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python3-Cython
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-numpy-devel >= %{numpy_ver}
BuildRequires:	python3-scipy >= %{scipy_ver}
BuildRequires:	python3-setuptools
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
%setup -q -n scikit-learn-%{version}

%build
%py3_build

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

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/sklearn/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/sklearn/{cluster,compose,covariance,cross_decomposition,datasets,decomposition,ensemble,ensemble/_hist_gradient_boosting,experimental,feature_extraction,feature_selection,gaussian_process,impute,inspection,linear_model,manifold,metrics,metrics/{_plot,cluster},mixture,model_selection,neighbors,neural_network,preprocessing,semi_supervised,svm,tree,utils}/tests

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
%dir %{py3_sitedir}/sklearn/cluster
%attr(755,root,root) %{py3_sitedir}/sklearn/cluster/_dbscan_inner.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/cluster/_hierarchical_fast.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/cluster/_k_means_elkan.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/cluster/_k_means_fast.cpython-*.so
%{py3_sitedir}/sklearn/cluster/*.py
%{py3_sitedir}/sklearn/cluster/__pycache__
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
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/_gradient_boosting.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/_loss.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/_predictor.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/common.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/histogram.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/splitting.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/utils.cpython-*.so
%{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/*.pxd
%{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/*.py
%{py3_sitedir}/sklearn/ensemble/_hist_gradient_boosting/__pycache__
%{py3_sitedir}/sklearn/experimental
%dir %{py3_sitedir}/sklearn/externals
%{py3_sitedir}/sklearn/externals/*.py
%{py3_sitedir}/sklearn/externals/__pycache__
%dir %{py3_sitedir}/sklearn/externals/joblib
%{py3_sitedir}/sklearn/externals/joblib/*.py
%{py3_sitedir}/sklearn/externals/joblib/__pycache__
%dir %{py3_sitedir}/sklearn/feature_extraction
%attr(755,root,root) %{py3_sitedir}/sklearn/feature_extraction/_hashing_fast.cpython-*.so
%{py3_sitedir}/sklearn/feature_extraction/*.py
%{py3_sitedir}/sklearn/feature_extraction/__pycache__
%{py3_sitedir}/sklearn/feature_selection
%{py3_sitedir}/sklearn/gaussian_process
%{py3_sitedir}/sklearn/impute
%{py3_sitedir}/sklearn/inspection
%dir %{py3_sitedir}/sklearn/linear_model
%attr(755,root,root) %{py3_sitedir}/sklearn/linear_model/_cd_fast.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/linear_model/_sag_fast.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/linear_model/_sgd_fast.cpython-*.so
%{py3_sitedir}/sklearn/linear_model/*.pxd
%{py3_sitedir}/sklearn/linear_model/*.py
%{py3_sitedir}/sklearn/linear_model/__pycache__
%dir %{py3_sitedir}/sklearn/manifold
%attr(755,root,root) %{py3_sitedir}/sklearn/manifold/_barnes_hut_tsne.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/manifold/_utils.cpython-*.so
%{py3_sitedir}/sklearn/manifold/*.py
%{py3_sitedir}/sklearn/manifold/__pycache__
%dir %{py3_sitedir}/sklearn/metrics
%attr(755,root,root) %{py3_sitedir}/sklearn/metrics/_pairwise_fast.cpython-*.so
%{py3_sitedir}/sklearn/metrics/*.py
%{py3_sitedir}/sklearn/metrics/__pycache__
%{py3_sitedir}/sklearn/metrics/_plot
%dir %{py3_sitedir}/sklearn/metrics/cluster
%attr(755,root,root) %{py3_sitedir}/sklearn/metrics/cluster/_expected_mutual_info_fast.cpython-*.so
%{py3_sitedir}/sklearn/metrics/cluster/*.py
%{py3_sitedir}/sklearn/metrics/cluster/__pycache__
%{py3_sitedir}/sklearn/mixture
%{py3_sitedir}/sklearn/model_selection
%dir %{py3_sitedir}/sklearn/neighbors
%attr(755,root,root) %{py3_sitedir}/sklearn/neighbors/_ball_tree.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/neighbors/_dist_metrics.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/neighbors/_kd_tree.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/neighbors/_quad_tree.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/neighbors/_typedefs.cpython-*.so
%{py3_sitedir}/sklearn/neighbors/*.pxd
%{py3_sitedir}/sklearn/neighbors/*.py
%{py3_sitedir}/sklearn/neighbors/__pycache__
%{py3_sitedir}/sklearn/neural_network
%dir %{py3_sitedir}/sklearn/preprocessing
%attr(755,root,root) %{py3_sitedir}/sklearn/preprocessing/_csr_polynomial_expansion.cpython-*.so
%{py3_sitedir}/sklearn/preprocessing/*.py
%{py3_sitedir}/sklearn/preprocessing/__pycache__
%{py3_sitedir}/sklearn/semi_supervised
%dir %{py3_sitedir}/sklearn/svm
%attr(755,root,root) %{py3_sitedir}/sklearn/svm/_liblinear.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/svm/_libsvm.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/svm/_libsvm_sparse.cpython-*.so
%{py3_sitedir}/sklearn/svm/*.py
%{py3_sitedir}/sklearn/svm/__pycache__
%dir %{py3_sitedir}/sklearn/tree
%attr(755,root,root) %{py3_sitedir}/sklearn/tree/_criterion.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/tree/_splitter.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/tree/_tree.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/tree/_utils.cpython-*.so
%{py3_sitedir}/sklearn/tree/*.pxd
%{py3_sitedir}/sklearn/tree/*.py
%{py3_sitedir}/sklearn/tree/__pycache__
%dir %{py3_sitedir}/sklearn/utils
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_cython_blas.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_fast_dict.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_logistic_sigmoid.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_openmp_helpers.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_random.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_seq_dataset.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_weight_vector.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/arrayfuncs.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/graph_shortest_path.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/murmurhash.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/sparsefuncs_fast.cpython-*.so
%{py3_sitedir}/sklearn/utils/*.pxd
%{py3_sitedir}/sklearn/utils/*.py
%{py3_sitedir}/sklearn/utils/__pycache__
%{py3_sitedir}/scikit_learn-%{version}-py*.egg-info
