%global module_name pyo

Name:		python-%{module_name}
Version:	0.6.9
Release:	4%{?dist}
Summary:	Python digital signal processing module

License:	GPLv3
URL:		http://ajaxsoundstudio.com/software/pyo/
Source0:	http://ajaxsoundstudio.com/downloads/%{module_name}_%{version}-src.tar.bz2
# COPYING.txt will be included in source tarballs from the next release:
# https://code.google.com/p/pyo/source/detail?r=1203
Source1:	COPYING.txt

BuildRequires:	python2-devel
BuildRequires:	liblo-devel
BuildRequires:	portaudio-devel
BuildRequires:	portmidi-devel
BuildRequires:	libsndfile-devel

%description
Pyo is a Python module written in C to help DSP script creation. Pyo contains
classes for a wide variety of audio signal processing. With pyo, the user will
be able to include signal processing chains directly in Python scripts or
projects, and to manipulate them in real time through the interpreter. Tools in
the pyo module offer primitives, like mathematical operations on audio signals,
basic signal processing (filters, delays, synthesis generators, etc.), but also
complex algorithms to create sound granulation and other creative audio
manipulations. pyo supports the OSC protocol (Open Sound Control) to ease
communications between softwares, and the MIDI protocol for generating sound
events and controlling process parameters. pyo allows the creation of
sophisticated signal processing chains with all the benefits of a mature, and
widely used, general programming language.

%prep
%setup -qn %{module_name}_%{version}-src
cp -p %{SOURCE1} .

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
%{__python2} setup.py install -O1 --use-jack --skip-build --prefix=%{_prefix} --root %{buildroot}
chmod 0755 %{buildroot}%{python2_sitearch}/_pyo.so

 
%files
%doc ChangeLog COPYING.txt
%{python2_sitearch}/*


%changelog
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
