%define git_repo django-ajax-selects
%define git_head HEAD

%define realname django-ajax-selects
%define name    python-%{realname}

Name:           %{name}
Version:	%git_get_ver
Release:        %mkrel %git_get_rel
Summary:        jQuery-powered auto-complete fields for ForeignKey and ManyToMany fields
Group:          Development/Python
License:        MIT and GPLv3
URL:            http://pypi.python.org/pypi/django-ajax-selects
Source:         %git_bs_source %{name}-%{version}.tar.gz
Source1:	%{name}-gitrpm.version
Source2:	%{name}-changelog.gitrpm.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
Enables editing of `ForeignKey`, `ManyToMany` and simple text fields using the
Autocomplete - `jQuery` plugin.

django-ajax-selects will work in any normal form as well as in the admin.

The user is presented with a text field. They type a search term or a few
letters of a name they are looking for, an ajax request is sent to the server,
a search channel returns possible results. Results are displayed as a drop down
menu. When an item is selected it is added to a display area just below the
text field.

%prep
%git_get_source
%setup -q

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}/usr/templates

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md ajax_select/LICENSE.txt
%{py_puresitedir}/ajax_select
%{py_puresitedir}/django_ajax_selects-%{version}-py%{pyver}.egg-info

%changelog -f %{_sourcedir}/%{name}-changelog.gitrpm.txt

