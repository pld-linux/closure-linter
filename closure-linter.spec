Summary:	Closure Linter - a style checker for JavaScript
Name:		closure-linter
Version:	2.3
Release:	1
License:	Apache v2.0
Group:		Applications/WWW
Source0:	https://closure-linter.googlecode.com/files/closure_linter-%{version}.tar.gz
# Source0-md5:	fcf40eba81428d2d1e92cc97d2f66fde
URL:		https://code.google.com/intl/en/closure/utilities/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
# distribute module for for pkg_resources
Requires:	python-distribute
Requires:	python-gflags
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Closure Linter is a utility that checks JavaScript files for style
issues such as operator placement, missing semicolons, spacing, the
presence of JsDoc annotations, and more.

%prep
%setup -qn closure_linter-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# fixjsstyle - tries to fix errors automatically
%attr(755,root,root) %{_bindir}/fixjsstyle
# gjslint - runs the linter and checks for errors
%attr(755,root,root) %{_bindir}/gjslint

%{py_sitescriptdir}/closure_linter
# egg always installed, even in py 2.4
%{py_sitescriptdir}/closure_linter-%{version}-py*.egg-info
