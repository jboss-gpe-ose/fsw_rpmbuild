Name:           fsw
Version:        6.0.0
Release:        1%{?dist}
Summary:        Red Hat JBoss Fuse Service Works (FSW)
Group:          Red Hat JBoss
License:        GPLv3+
URL:            http://www.redhat.com
Source0:        fsw-modules-6.0.0.GA-redhat-4.zip
Source1:        fsw-deployments-6.0.0.GA-redhat-4.zip
Requires:       jboss_bpm_soa = 6.1.1

%description

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/jboss_bpm_soa/jboss-eap-6.1/modules/system/layers
unzip %{SOURCE0} -d $RPM_BUILD_ROOT/opt/jboss_bpm_soa/jboss-eap-6.1/modules/system/layers
mkdir -p $RPM_BUILD_ROOT/opt/jboss_bpm_soa/jboss-eap-6.1/standalone/deployments
unzip %{SOURCE1} -d $RPM_BUILD_ROOT/opt/jboss_bpm_soa/jboss-eap-6.1/standalone/deployments

%clean
rm -rf $RPM_BUILD_ROOT

%post
# ensure compatibility with FSW
echo "layers=bpms,soa,sramp" > /opt/jboss_bpm_soa/jboss-eap-6.1/modules/layers.conf

%files
/opt/jboss_bpm_soa/jboss-eap-6.1/*
