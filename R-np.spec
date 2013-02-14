%global packname  np
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.40.13
Release:          1
Summary:          Nonparametric kernel smoothing methods for mixed data types
Group:            Sciences/Mathematics
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/np_0.40-13.tar.gz
Requires:         R-boot R-cubature 
Requires:         R-quantreg R-MASS 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-boot R-cubature
BuildRequires:    R-quantreg R-MASS 
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
This package provides a variety of nonparametric (and semiparametric)
kernel methods that seamlessly handle a mix of continuous, unordered, and
ordered factor data types. We would like to gratefully acknowledge support
from the Natural Sciences and Engineering Research Council of Canada
(NSERC:www.nserc.ca), the Social Sciences and Humanities Research Council
of Canada (SSHRC:www.sshrc.ca), and the Shared Hierarchical Academic
Research Computing Network (SHARCNET:www.sharcnet.ca).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# FIXME killed after 15 min at 100%% cpp ...
%if 0
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
