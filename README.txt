Purpose
  - package management of JBoss Business Process Management (BPMS) v6 on Red Hat Enterprise Linux (RHEL)

Build Procedure
  - ensure that 'jboss_bpm_soa' RPM has already been installed on target operating system
  - clone this project from github
  - download jboss-bpms-6.0.0-redhat-7-deployable-eap6.x.zip from Red Hat Customer Support Portal
  - cd /path/to/this/bpms_rpmbuild
  - cp /path/to/jboss-bpms-6.0.0-redhat-7-deployable-eap6.x.zip SOURCES
  - rpmbuild --define "_sourcedir `pwd`/SOURCES" -ba SPECS/bpms.spec
  - rpm -qlp ~/rpmbuild/RPMS/x86_64/bpms-6.0.0-1.el6.x86_64.rpm
  - sudo rpm -ivh --replacefiles ~/rpmbuild/RPMS/x86_64/bpms-6.0.0-1.el6.x86_64.rpm
    - NOTE:  
        - BPMS6 intentionally over-rides several configuration files from JBoss EAP6.1.1
        - writing over these files is safe and can be done with RPM via "--replacefiles" flag
    
  - sudo rpm -e bpms

 TO-DO
