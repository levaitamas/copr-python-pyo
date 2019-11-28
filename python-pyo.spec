%global pypi_name pyo

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        1%{?dist}
Summary:        Python module to build digital signal processing program

License:        LGPLv3+
URL:            http://ajaxsoundstudio.com/software/pyo/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

BuildRequires:	liblo-devel
BuildRequires:	portaudio-devel
BuildRequires:	portmidi-devel
BuildRequires:	libsndfile-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	gcc

%description
pyo is a Python module containing classes for a wide variety of audio signal
processing types. With pyo, user will be able to include signal processing
chains directly in Python scripts or projects, and to manipulate them in real
time through the interpreter. Tools in pyo module offer primitives, like
mathematical operations on audio signal, basic signal processing (filters,
delays, synthesis...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
Obsoletes: python-%{pypi_name}
Provides: python-%{pypi_name}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(setuptools)
%description -n python2-%{pypi_name}
pyo is a Python module containing classes for a wide variety of audio signal
processing types. With pyo, user will be able to include signal processing
chains directly in Python scripts or projects, and to manipulate them in real
time through the interpreter. Tools in pyo module offer primitives, like
mathematical operations on audio signal, basic signal processing (filters,
delays, synthesis...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Obsoletes: python-%{pypi_name}
Provides: python-%{pypi_name}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
pyo is a Python module containing classes for a wide variety of audio signal
processing types. With pyo, user will be able to include signal processing
chains directly in Python scripts or projects, and to manipulate them in real
time through the interpreter. Tools in pyo module offer primitives, like
mathematical operations on audio signal, basic signal processing (filters,
delays, synthesis...

%global debug_package %{nil}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build --use-jack --use-double
%{__python3} setup.py build --use-jack --use-double

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
rm -rf %{buildroot}%{_bindir}/*
%py3_install

%files -n python2-%{pypi_name}
%doc README.md
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}64
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.md
%{_bindir}/epyo
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}64
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Nov 28 2019 Tamas Levai <levait@tmit.bme.hu> 1.0.1-1
- Update to 1.0.1 (levait@tmit.bme.hu)

* Fri Jul 12 2019 Tamas Levai <levait@tmit.bme.hu> 1.0.0-1
- Update to 1.0.0 (levait@tmit.bme.hu)

* Thu May 09 2019 Tamas Levai <levait@tmit.bme.hu> 0.9.7-1
- Update to 0.9.7, build from sdist (levait@tmit.bme.hu)

* Wed Sep 05 2018 Tamas Levai <levait@tmit.bme.hu> 0.9.1-2
- Add GCC build dependency to fix Fedora 29 builds (levait@tmit.bme.hu)

* Wed Sep 05 2018 Tamas Levai <levait@tmit.bme.hu> 0.9.1-1
- Update to 0.9.1 (levait@tmit.bme.hu)
- Automatic commit of package [python-pyo] release [0.9.0-1].
  (levait@tmit.bme.hu)
- Update to 0.9.0 (levait@tmit.bme.hu)
- Automatic commit of package [python-pyo] release [0.8.9-1].
  (levait@tmit.bme.hu)
- Update to 0.8.9 (levait@tmit.bme.hu)

* Wed Feb 21 2018 Tamas Levai <levait@tmit.bme.hu> 0.9.0-1
- Update to 0.9.0 (levait@tmit.bme.hu)

* Sun Feb 04 2018 Tamas Levai <levait@tmit.bme.hu> 0.8.9-1
- Update to 0.8.9 (levait@tmit.bme.hu)

* Wed Nov 08 2017 Tamas Levai <levait@tmit.bme.hu> 0.8.8-1
- Update to 0.8.8 (levait@tmit.bme.hu)

* Tue Sep 12 2017 Tamas Levai <levait@tmit.bme.hu> 0.8.7-2
- Tweak spec file (levait@tmit.bme.hu)

* Tue Aug 29 2017 Tamas Levai <levait@tmit.bme.hu> 0.8.7-1
- Update to 0.8.7 (levait@tmit.bme.hu)

* Fri Apr 21 2017 Tamas Levai <levait@tmit.bme.hu> 0.8.6-1
- Update to 0.8.6 (levait@tmit.bme.hu)

* Sat Apr 01 2017 Tamas Levai <levait@tmit.bme.hu> 0.8.5-1
- Update to 0.8.5 (levait@tmit.bme.hu)

* Sat Mar 25 2017 Tamas Levai <levait@tmit.bme.hu> 0.8.4-1
- Update to 0.8.4 (levait@tmit.bme.hu)

* Mon Feb 13 2017 Tamas Levai <levait@tmit.bme.hu> 0.8.3-1
- Update to 0.8.3 (levait@tmit.bme.hu)

* Sun Dec 18 2016 Tamas Levai <levait@tmit.bme.hu> 0.8.2-1
- Update to 0.8.2 (levait@tmit.bme.hu)

* Mon Dec 12 2016 Tamas Levai <levait@tmit.bme.hu> 0.8.1-2
- Create package for both Python 2 and Python 3 (levait@tmit.bme.hu)

* Sun Dec 11 2016 Tamas Levai <levait@tmit.bme.hu> 0.8.1-1
- Update to 0.8.1 (levait@tmit.bme.hu)

* Sun Dec 11 2016 Tamas Levai <levait@tmit.bme.hu> 0.8.0-1
- new package built with tito

* Sun May 15 2016 Tamas Levai <levait@tmit.bme.hu> - 0.8.0
- Update to 0.8.0

* Tue Apr 26 2016 Tamas Levai <levait@tmit.bme.hu> - 0.7.9
- Update to 0.7.9
- Fix jack support
- Handle package name change

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 0.7.8-1
- Update to 0.7.8
- Enable jack support

* Sun Dec 06 2015 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 0.7.7-1
- Update to 0.7.7
- License changes from GPLv3 to LGPLv3+
- Provide python2- subpackage
- Modernize macros

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug 19 2014 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 0.6.9-3
- Removing duplicated file
- Changing to versioned BR python2-devel

* Mon Aug 18 2014 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 0.6.9-2
- Adding license file from upstream's SVN
- Fixing egg file name

* Mon Aug 11 2014 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 0.6.9-1
- Initial packaging
