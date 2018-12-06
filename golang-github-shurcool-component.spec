# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/component
%global commit          f88ec8f54cc4038bdd2c3b1aecf4b96c132d7beb

%global common_description %{expand:
Collection of basic HTML components.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Collection of basic HTML components
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/shurcooL/htmlg)
BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/net/html/atom)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitf88ec8f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420gitf88ec8f
- First package for Fedora

