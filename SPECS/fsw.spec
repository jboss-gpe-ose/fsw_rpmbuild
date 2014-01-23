Name:           fsw
Version:        1.1.1-p2-redhat-2
Release:        1%{?dist}
Summary:        Red Hat JBoss Fuse Service Works (FSW)
Group:          Red Hat JBoss
License:        GPLv3+
URL:            http://www.redhat.com
Source0:        fsw-modules-${Version}.zip
Requires:       jboss_bpm_soa = 6.1.1

%description

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/jboss_bpm_soa
unzip %{SOURCE0} -d $RPM_BUILD_ROOT/opt/jboss_bpm_soa/jboss-eap-6.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
# ensure compatibility with FSW
echo "layers=bpms,soa" > /opt/jboss_bpm_soa/jboss-eap-6.1/modules/layers.conf

%files
/opt/jboss_bpm_soa/jboss-eap-6.1/*
