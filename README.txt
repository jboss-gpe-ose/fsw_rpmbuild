Purpose
  - package management of Red Hat JBoss Fuse Service Works (FSW) v6 on Red Hat Enterprise Linux (RHEL)

Build Procedure
  - ensure that 'jboss_bpm_soa' RPM has already been installed on target operating system
  - clone this project from github
  - download jboss-fsw-installer-6.0.0.GA-redhat-4.jar from http://dev138.mw.lab.eng.bos.redhat.com/candidate/soa-6.0.0-CR4/
  - java -jar jboss-fsw-installer-6.0.0.GA-redhat-4.jar
    - go through manual installation process
    - zip and copy FSW modules and web archives to SOURCES directory
  - cd /path/to/this/fsw_rpmbuild
  - rpmbuild --define "_sourcedir `pwd`/SOURCES" -ba SPECS/fsw.spec
  - rpm -qlp ~/rpmbuild/RPMS/x86_64/fsw-6.0.0-1.el6.x86_64.rpm
  - sudo rpm -ivh --replacefiles ~/rpmbuild/RPMS/x86_64/fsw-6.0.0-1.el6.x86_64.rpm
    - NOTE:  
        - FSW intentionally over-rides several configuration files from JBoss EAP6.1.1
        - writing over these files is safe and can be done with RPM via "--replacefiles" flag
    
  - sudo rpm -e fsw

 TO-DO
