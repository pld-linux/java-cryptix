%define 	snapshot	20001002

Summary:	Java crypto package
Name:		cryptix
Version:	3.2.0
Release:	1
License:	BSD style
URL:		http://www.cryptix.org
Group:		Development/Languages/Java
Source0:	http://www.cryptix.org/dist/%{name}32-%{snapshot}-r%{version}.zip
# Source0-md5:	7a3545ede3fff5c89eba601fea03791a
Source1:	%{name}.build.xml
BuildRequires:	jakarta-ant >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
Cryptix 3 is a cleanroom implementation of Sun's Java Cryptography
Extensions (JCE) version 1.1. In addition to that it contains the
Cryptix Provider which delivers a wide range of algorithms and support
for PGP 2.x. Cryptix 3 runs on both JDK 1.1 and JDK 1.2 (Java 2).

%prep
%setup -q -c
cp %{SOURCE1} build.xml
find . -name "*.jar" -exec rm -f {} \;

%build
ant jar
ant javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}
cp build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf %{name}.jar $RPM_BUILD_ROOT/%{_javalibdir}/%{name}-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE.TXT README.TXT build/api
%{_javalibdir}/*.jar
