%bcond_without	javadoc		# build api docs

%define 	snapshot	20001002
%define		srcname		cryptix
Summary:	Java crypto package
Summary(pl.UTF-8):	Pakiet kryptograficzny Javy
Name:		java-cryptix
Version:	3.2.0
Release:	2
License:	BSD-like
Group:		Libraries/Java
Source0:	http://www.cryptix.org/dist/%{srcname}32-%{snapshot}-r%{version}.zip
# Source0-md5:	7a3545ede3fff5c89eba601fea03791a
Source1:	%{srcname}.build.xml
Patch0:		%{srcname}-java-1.5.patch
URL:		http://www.cryptix.org/
BuildRequires:	ant >= 1.5
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	jre >= 1.1
Obsoletes:	cryptix
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cryptix 3 is a cleanroom implementation of Sun's Java Cryptography
Extensions (JCE) version 1.1. In addition to that it contains the
Cryptix Provider which delivers a wide range of algorithms and support
for PGP 2.x. Cryptix 3 runs on both JDK 1.1 and JDK 1.2 (Java 2).

%description -l pl.UTF-8
Cryptix 3 to implementacja standardu JCE (Java Cryptography
Extensions) Suna w wersji 1.1. Pakiet dodatkowo zawiera Cryptix
Provider, dostarczający szeroki zakres algorytmów oraz wsparcie dla
PGP 2.x. Cryptix 3 działa zarówno na JDK 1.1 jak i JDK 1.2 (Java 2).

%package javadoc
Summary:	Online manual for %{srcname}
Summary(pl.UTF-8):	Dokumentacja online do %{srcname}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{srcname}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{srcname}.

%description javadoc -l fr.UTF-8
Javadoc pour %{srcname}.

%prep
%setup -q -c
%patch0 -p1
cp %{SOURCE1} build.xml
find -name '*.jar' | xargs rm -v

%build
%ant jar %{?with_javadoc:javadoc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp build/lib/%{srcname}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -sf %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc LICENCE.TXT README.TXT build/api
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
