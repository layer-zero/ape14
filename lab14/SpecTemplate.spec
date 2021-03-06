# RPM Preamble
Summary:        Your Description Here
Name:           MyRPM
Version:        1
Release:        0
URL:            http://www.class.com
BuildArch:      noarch
Source0:        %{name}-%{version}-%{release}.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:       /bin/bash
License:        Creative Commons
# Disable auto-dependencies (lame way of using /bin/bash)
#AutoReqProv:   no


# Description of the package
%description
Describe your package here

%prep
# Gunzip the files, create the dir (-c) in BUILD and put them there
%setup -c

%build

%install
  # ${RPM_BUILD_ROOT} is the same as %{buildroot}
  rm -rf   %{buildroot}
  mkdir -p %{buildroot}%{_optdir}
  cp -Rp * %{buildroot}%{_optdir}

%clean
 rm -rf %{buildroot}

%files
 %defattr(777,root,root,777)
 # Specifying the directories individually gives them the right mod
# %dir %{_optdir}/
 %dir %{_optdir}/%{name}/
 # ex: %dir %{_optdir}/%{name}/bin/
 # ex: %dir %{_optdir}/%{name}/data/

%post
 # Run after files are installed

 # Install links and CLI Aliases (if EOS)
 # ex:  %{_optdir}/%{name}/bin/cpuhist install

%preun
 #This runs before the RPM is uninstalled

 # Stop the daemons
 # ex: %{_optdir}/%{name}/bin/cpuhist stop

%postun
 # This runs after the RPM is uninstalled
