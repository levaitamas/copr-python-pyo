%global module_name pyo

Name:		python-%{module_name}
Version:	0.8.7
Release:	1%{?dist}
Summary:	Python digital signal processing module

License:	GPLv3+
URL:		http://ajaxsoundstudio.com/software/pyo/
Source0:	http://ajaxsoundstudio.com/downloads/%{module_name}_%{version}-src.tar.bz2

%description
Pyo is a Python module written in C to help DSP script creation. Pyo
contains classes for a wide variety of audio signal processing. With
pyo, the user will be able to include signal processing chains
directly in Python scripts or projects, and to manipulate them in real
time through the interpreter. Tools in the pyo module offer
primitives, like mathematical operations on audio signals, basic
signal processing (filters, delays, synthesis generators, etc.), but
also complex algorithms to create sound granulation and other creative
audio manipulations. pyo supports the OSC protocol (Open Sound
Control) to ease communications between softwares, and the MIDI
protocol for generating sound events and controlling process
parameters. pyo allows the creation of sophisticated signal processing
chains with all the benefits of a mature and widely used general
programming language.

%package -n python2-%{module_name}
Summary:	%{summary}
BuildRequires:	python2-devel
BuildRequires:	liblo-devel
BuildRequires:	portaudio-devel
BuildRequires:	portmidi-devel
BuildRequires:	libsndfile-devel
BuildRequires:	jack-audio-connection-kit-devel
Obsoletes: python-%{module_name}
Provides: python-%{module_name}
%{?python_provide:%python_provide python2-%{module_name}}

%description -n python2-%{module_name}
Python 2 version.

%package -n python3-%{module_name}
Summary:	%{summary}
BuildRequires:	python3-devel
BuildRequires:	liblo-devel
BuildRequires:	portaudio-devel
BuildRequires:	portmidi-devel
BuildRequires:	libsndfile-devel
BuildRequires:	jack-audio-connection-kit-devel
Obsoletes: python-%{module_name}
Provides: python-%{module_name}
%{?python_provide:%python_provide python3-%{module_name}}

%description -n python3-%{module_name}
Python 3 version.

%prep
%setup -qn %{module_name}_%{version}-src

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build --use-jack --use-double
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build --use-jack --use-double

%install
%py2_install
%py3_install
chmod 0755 %{buildroot}%{python2_sitearch}/_pyo.so

%files -n python2-%{module_name}
%license COPYING.txt
%doc ChangeLog
%{python2_sitearch}/*

%files -n python3-%{module_name}
%license COPYING.txt
%doc ChangeLog
%{python3_sitearch}/*


%changelog
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
