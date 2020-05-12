# NOTE: for versions >= 0.21 (for python 3.5+) see python3-scikit-learn.spec
# TODO:
# - system libs:
#   - cblas/atlas everywhere (now some parts use system, but included cblas is compiled too)
#   - libsvm, liblinear
#   - python modules in externals: _arff _pilutil funcsigs six joblib [cloudpickle loky]
# - test failures (a few with python2, cannot run with python3)
#
# Conditional build:
%bcond_with	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define	numpy_ver	1.8.2
%define	scipy_ver	0.13.3

Summary:	Set of Python 2 modules for machine learning and data mining
Summary(pl.UTF-8):	Zbiór modułów Pythona 2 do uczenia maszynowego i eksporacji danych
Name:		python-scikit-learn
# NOTE: keep 0.20.x here, 0.21+ don't support python2
Version:	0.20.4
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/scikit-learn/
Source0:	https://files.pythonhosted.org/packages/source/s/scikit-learn/scikit-learn-%{version}.tar.gz
# Source0-md5:	f0c44f397738ea1140a596f74592400e
URL:		https://scikit-learn.org/
BuildRequires:	cblas-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
#BuildRequires:	python-Cython
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-numpy-devel >= %{numpy_ver}
BuildRequires:	python-scipy >= %{scipy_ver}
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest >= 3.3.0
%endif
%endif
%if %{with python3}
#BuildRequires:	python3-Cython
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-numpy-devel >= %{numpy_ver}
BuildRequires:	python3-scipy >= %{scipy_ver}
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 3.3.0
%endif
%endif
Requires:	python-modules >= 1:2.7
Requires:	python-numpy >= %{numpy_ver}
Requires:	python-scipy >= %{scipy_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

%description -l pl.UTF-8
scikit-learn to moduł Pythona do uczenia maszynowego, zbudowany w
oparciu o SciPy i rozprowadzany na 3-punktowej licencji BSD.

%package -n python3-scikit-learn
Summary:	Set of Python 2 modules for machine learning and data mining
Summary(pl.UTF-8):	Zbiór modułów Pythona 2 do uczenia maszynowego i eksporacji danych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4
Requires:	python3-numpy >= %{numpy_ver}
Requires:	python3-scipy >= %{scipy_ver}

%description -n python3-scikit-learn
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

%description -n python3-scikit-learn -l pl.UTF-8
scikit-learn to moduł Pythona do uczenia maszynowego, zbudowany w
oparciu o SciPy i rozprowadzany na 3-punktowej licencji BSD.

%prep
%setup -q -n scikit-learn-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
cd build-2/lib.*
ln -snf ../../../../sklearn/datasets/data sklearn/datasets/data
ln -snf ../../../../sklearn/datasets/descr sklearn/datasets/descr
ln -snf ../../../../sklearn/datasets/images sklearn/datasets/images
ln -snf ../../../../../sklearn/datasets/tests/data sklearn/datasets/tests/data
%{__python} -m pytest
%{__rm} sklearn/datasets/{data,descr,images} sklearn/datasets/tests/data
cd ../..
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
cd build-3/lib.*
ln -snf ../../../../sklearn/datasets/data sklearn/datasets/data
ln -snf ../../../../sklearn/datasets/descr sklearn/datasets/descr
ln -snf ../../../../sklearn/datasets/images sklearn/datasets/images
ln -snf ../../../../../sklearn/datasets/tests/data sklearn/datasets/tests/data
%{__python3} -m pytest
%{__rm} sklearn/datasets/{data,descr,images} sklearn/datasets/tests/data
cd ../..
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/sklearn/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/sklearn/{cluster,compose,covariance,cross_decomposition,datasets,decomposition,ensemble,feature_extraction,feature_selection,gaussian_process,linear_model,manifold,metrics,metrics/cluster,mixture,model_selection,neighbors,neural_network,preprocessing,semi_supervised,svm,tree,utils,utils/sparsetools}/tests
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/sklearn/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/sklearn/{cluster,compose,covariance,cross_decomposition,datasets,decomposition,ensemble,feature_extraction,feature_selection,gaussian_process,linear_model,manifold,metrics,metrics/cluster,mixture,model_selection,neighbors,neural_network,preprocessing,semi_supervised,svm,tree,utils,utils/sparsetools}/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc COPYING README.rst
%dir %{py_sitedir}/sklearn
%attr(755,root,root%) %{py_sitedir}/sklearn/_isotonic.so
%attr(755,root,root%) %{py_sitedir}/sklearn/*.py[co]
%dir %{py_sitedir}/sklearn/__check_build
%attr(755,root,root) %{py_sitedir}/sklearn/__check_build/_check_build.so
%{py_sitedir}/sklearn/__check_build/*.py[co]
%{py_sitedir}/sklearn/_build_utils
%dir %{py_sitedir}/sklearn/cluster
%attr(755,root,root) %{py_sitedir}/sklearn/cluster/_dbscan_inner.so
%attr(755,root,root) %{py_sitedir}/sklearn/cluster/_hierarchical.so
%attr(755,root,root) %{py_sitedir}/sklearn/cluster/_k_means.so
%attr(755,root,root) %{py_sitedir}/sklearn/cluster/_k_means_elkan.so
%{py_sitedir}/sklearn/cluster/*.py[co]
%{py_sitedir}/sklearn/compose
%{py_sitedir}/sklearn/covariance
%{py_sitedir}/sklearn/cross_decomposition
%dir %{py_sitedir}/sklearn/datasets
%attr(755,root,root) %{py_sitedir}/sklearn/datasets/_svmlight_format.so
%{py_sitedir}/sklearn/datasets/*.py[co]
%{py_sitedir}/sklearn/datasets/data
%{py_sitedir}/sklearn/datasets/descr
%{py_sitedir}/sklearn/datasets/images
%dir %{py_sitedir}/sklearn/decomposition
%attr(755,root,root) %{py_sitedir}/sklearn/decomposition/_online_lda.so
%attr(755,root,root) %{py_sitedir}/sklearn/decomposition/cdnmf_fast.so
%{py_sitedir}/sklearn/decomposition/*.py[co]
%dir %{py_sitedir}/sklearn/ensemble
%attr(755,root,root) %{py_sitedir}/sklearn/ensemble/_gradient_boosting.so
%{py_sitedir}/sklearn/ensemble/*.py[co]
%dir %{py_sitedir}/sklearn/externals
%{py_sitedir}/sklearn/externals/*.py[co]
%dir %{py_sitedir}/sklearn/externals/joblib
%{py_sitedir}/sklearn/externals/joblib/*.py[co]
%dir %{py_sitedir}/sklearn/externals/joblib/externals
%{py_sitedir}/sklearn/externals/joblib/externals/__init__.py[co]
%{py_sitedir}/sklearn/externals/joblib/externals/cloudpickle
%{py_sitedir}/sklearn/externals/joblib/externals/loky
%dir %{py_sitedir}/sklearn/feature_extraction
%attr(755,root,root) %{py_sitedir}/sklearn/feature_extraction/_hashing.so
%{py_sitedir}/sklearn/feature_extraction/*.py[co]
%{py_sitedir}/sklearn/feature_selection
%{py_sitedir}/sklearn/gaussian_process
%dir %{py_sitedir}/sklearn/linear_model
%attr(755,root,root) %{py_sitedir}/sklearn/linear_model/cd_fast.so
%attr(755,root,root) %{py_sitedir}/sklearn/linear_model/sag_fast.so
%attr(755,root,root) %{py_sitedir}/sklearn/linear_model/sgd_fast.so
%{py_sitedir}/sklearn/linear_model/*.py[co]
%dir %{py_sitedir}/sklearn/manifold
%attr(755,root,root) %{py_sitedir}/sklearn/manifold/_barnes_hut_tsne.so
%attr(755,root,root) %{py_sitedir}/sklearn/manifold/_utils.so
%{py_sitedir}/sklearn/manifold/*.py[co]
%dir %{py_sitedir}/sklearn/metrics
%attr(755,root,root) %{py_sitedir}/sklearn/metrics/pairwise_fast.so
%{py_sitedir}/sklearn/metrics/*.py[co]
%dir %{py_sitedir}/sklearn/metrics/cluster
%attr(755,root,root) %{py_sitedir}/sklearn/metrics/cluster/expected_mutual_info_fast.so
%{py_sitedir}/sklearn/metrics/cluster/*.py[co]
%{py_sitedir}/sklearn/mixture
%{py_sitedir}/sklearn/model_selection
%dir %{py_sitedir}/sklearn/neighbors
%attr(755,root,root) %{py_sitedir}/sklearn/neighbors/ball_tree.so
%attr(755,root,root) %{py_sitedir}/sklearn/neighbors/dist_metrics.so
%attr(755,root,root) %{py_sitedir}/sklearn/neighbors/kd_tree.so
%attr(755,root,root) %{py_sitedir}/sklearn/neighbors/quad_tree.so
%attr(755,root,root) %{py_sitedir}/sklearn/neighbors/typedefs.so
%{py_sitedir}/sklearn/neighbors/*.py[co]
%{py_sitedir}/sklearn/neural_network
%{py_sitedir}/sklearn/preprocessing
%{py_sitedir}/sklearn/semi_supervised
%dir %{py_sitedir}/sklearn/svm
%attr(755,root,root) %{py_sitedir}/sklearn/svm/liblinear.so
%attr(755,root,root) %{py_sitedir}/sklearn/svm/libsvm.so
%attr(755,root,root) %{py_sitedir}/sklearn/svm/libsvm_sparse.so
%{py_sitedir}/sklearn/svm/*.py[co]
%dir %{py_sitedir}/sklearn/tree
%attr(755,root,root) %{py_sitedir}/sklearn/tree/_criterion.so
%attr(755,root,root) %{py_sitedir}/sklearn/tree/_splitter.so
%attr(755,root,root) %{py_sitedir}/sklearn/tree/_tree.so
%attr(755,root,root) %{py_sitedir}/sklearn/tree/_utils.so
%{py_sitedir}/sklearn/tree/*.pxd
%{py_sitedir}/sklearn/tree/*.py[co]
%dir %{py_sitedir}/sklearn/utils
%attr(755,root,root) %{py_sitedir}/sklearn/utils/_logistic_sigmoid.so
%attr(755,root,root) %{py_sitedir}/sklearn/utils/_random.so
%attr(755,root,root) %{py_sitedir}/sklearn/utils/arrayfuncs.so
%attr(755,root,root) %{py_sitedir}/sklearn/utils/fast_dict.so
%attr(755,root,root) %{py_sitedir}/sklearn/utils/graph_shortest_path.so
%attr(755,root,root) %{py_sitedir}/sklearn/utils/lgamma.so
%attr(755,root,root) %{py_sitedir}/sklearn/utils/murmurhash.so
%attr(755,root,root) %{py_sitedir}/sklearn/utils/seq_dataset.so
%attr(755,root,root) %{py_sitedir}/sklearn/utils/sparsefuncs_fast.so
%attr(755,root,root) %{py_sitedir}/sklearn/utils/weight_vector.so
%{py_sitedir}/sklearn/utils/*.py[co]
%{py_sitedir}/sklearn/utils/sparsetools
%{py_sitedir}/scikit_learn-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-scikit-learn
%defattr(644,root,root,755)
%doc COPYING README.rst
%dir %{py3_sitedir}/sklearn
%attr(755,root,root%) %{py3_sitedir}/sklearn/_isotonic.cpython-*.so
%attr(755,root,root%) %{py3_sitedir}/sklearn/*.py
%attr(755,root,root%) %{py3_sitedir}/sklearn/__pycache__
%dir %{py3_sitedir}/sklearn/__check_build
%attr(755,root,root) %{py3_sitedir}/sklearn/__check_build/_check_build.cpython-*.so
%{py3_sitedir}/sklearn/__check_build/*.py
%{py3_sitedir}/sklearn/__check_build/__pycache__
%{py3_sitedir}/sklearn/_build_utils
%dir %{py3_sitedir}/sklearn/cluster
%attr(755,root,root) %{py3_sitedir}/sklearn/cluster/_dbscan_inner.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/cluster/_hierarchical.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/cluster/_k_means.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/cluster/_k_means_elkan.cpython-*.so
%{py3_sitedir}/sklearn/cluster/*.py
%{py3_sitedir}/sklearn/cluster/__pycache__
%{py3_sitedir}/sklearn/compose
%{py3_sitedir}/sklearn/covariance
%{py3_sitedir}/sklearn/cross_decomposition
%dir %{py3_sitedir}/sklearn/datasets
%attr(755,root,root) %{py3_sitedir}/sklearn/datasets/_svmlight_format.cpython-*.so
%{py3_sitedir}/sklearn/datasets/*.py
%{py3_sitedir}/sklearn/datasets/__pycache__
%{py3_sitedir}/sklearn/datasets/data
%{py3_sitedir}/sklearn/datasets/descr
%{py3_sitedir}/sklearn/datasets/images
%dir %{py3_sitedir}/sklearn/decomposition
%attr(755,root,root) %{py3_sitedir}/sklearn/decomposition/_online_lda.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/decomposition/cdnmf_fast.cpython-*.so
%{py3_sitedir}/sklearn/decomposition/*.py
%{py3_sitedir}/sklearn/decomposition/__pycache__
%dir %{py3_sitedir}/sklearn/ensemble
%attr(755,root,root) %{py3_sitedir}/sklearn/ensemble/_gradient_boosting.cpython-*.so
%{py3_sitedir}/sklearn/ensemble/*.py
%{py3_sitedir}/sklearn/ensemble/__pycache__
%dir %{py3_sitedir}/sklearn/externals
%{py3_sitedir}/sklearn/externals/*.py
%{py3_sitedir}/sklearn/externals/__pycache__
%dir %{py3_sitedir}/sklearn/externals/joblib
%{py3_sitedir}/sklearn/externals/joblib/*.py
%{py3_sitedir}/sklearn/externals/joblib/__pycache__
%dir %{py3_sitedir}/sklearn/externals/joblib/externals
%{py3_sitedir}/sklearn/externals/joblib/externals/__init__.py
%{py3_sitedir}/sklearn/externals/joblib/externals/__pycache__
%{py3_sitedir}/sklearn/externals/joblib/externals/cloudpickle
%{py3_sitedir}/sklearn/externals/joblib/externals/loky
%dir %{py3_sitedir}/sklearn/feature_extraction
%attr(755,root,root) %{py3_sitedir}/sklearn/feature_extraction/_hashing.cpython-*.so
%{py3_sitedir}/sklearn/feature_extraction/*.py
%{py3_sitedir}/sklearn/feature_extraction/__pycache__
%{py3_sitedir}/sklearn/feature_selection
%{py3_sitedir}/sklearn/gaussian_process
%dir %{py3_sitedir}/sklearn/linear_model
%attr(755,root,root) %{py3_sitedir}/sklearn/linear_model/cd_fast.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/linear_model/sag_fast.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/linear_model/sgd_fast.cpython-*.so
%{py3_sitedir}/sklearn/linear_model/*.py
%{py3_sitedir}/sklearn/linear_model/__pycache__
%dir %{py3_sitedir}/sklearn/manifold
%attr(755,root,root) %{py3_sitedir}/sklearn/manifold/_barnes_hut_tsne.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/manifold/_utils.cpython-*.so
%{py3_sitedir}/sklearn/manifold/*.py
%{py3_sitedir}/sklearn/manifold/__pycache__
%dir %{py3_sitedir}/sklearn/metrics
%attr(755,root,root) %{py3_sitedir}/sklearn/metrics/pairwise_fast.cpython-*.so
%{py3_sitedir}/sklearn/metrics/*.py
%{py3_sitedir}/sklearn/metrics/__pycache__
%dir %{py3_sitedir}/sklearn/metrics/cluster
%attr(755,root,root) %{py3_sitedir}/sklearn/metrics/cluster/expected_mutual_info_fast.cpython-*.so
%{py3_sitedir}/sklearn/metrics/cluster/*.py
%{py3_sitedir}/sklearn/metrics/cluster/__pycache__
%{py3_sitedir}/sklearn/mixture
%{py3_sitedir}/sklearn/model_selection
%dir %{py3_sitedir}/sklearn/neighbors
%attr(755,root,root) %{py3_sitedir}/sklearn/neighbors/ball_tree.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/neighbors/dist_metrics.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/neighbors/kd_tree.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/neighbors/quad_tree.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/neighbors/typedefs.cpython-*.so
%{py3_sitedir}/sklearn/neighbors/*.py
%{py3_sitedir}/sklearn/neighbors/__pycache__
%{py3_sitedir}/sklearn/neural_network
%{py3_sitedir}/sklearn/preprocessing
%{py3_sitedir}/sklearn/semi_supervised
%dir %{py3_sitedir}/sklearn/svm
%attr(755,root,root) %{py3_sitedir}/sklearn/svm/liblinear.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/svm/libsvm.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/svm/libsvm_sparse.cpython-*.so
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
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_logistic_sigmoid.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/_random.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/arrayfuncs.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/fast_dict.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/graph_shortest_path.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/lgamma.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/murmurhash.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/seq_dataset.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/sparsefuncs_fast.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sklearn/utils/weight_vector.cpython-*.so
%{py3_sitedir}/sklearn/utils/*.py
%{py3_sitedir}/sklearn/utils/__pycache__
%{py3_sitedir}/sklearn/utils/sparsetools
%{py3_sitedir}/scikit_learn-%{version}-py*.egg-info
%endif
