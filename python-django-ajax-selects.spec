%define realname django-ajax-selects
%define name    python-%{realname}
%define version 1.1.4
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        jQuery-powered auto-complete fields for ForeignKey and ManyToMany fields
Group:          Development/Python
License:        MIT and GPLv3
URL:            http://pypi.python.org/pypi/django-ajax-selects
Source:         http://pypi.python.org/packages/source/d/django-ajax-selects/%{realname}-%{version}.tar.gz
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
%setup -q -n %{realname}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}/usr/templates

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt ajax_select/LICENSE.txt ajax_select/docs.txt
%{py_puresitedir}/ajax_select
%{py_puresitedir}/django_ajax_selects-%{version}-py%{pyver}.egg-info


