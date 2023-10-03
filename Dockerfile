FROM oraclelinux:7-slim

#  Install wget utility.
RUN yum install -y wget

RUN yum install -y gzip

# Download Oracle Database Express Edition (XE) Release 18.4.0.0.0 (18c) RPM package
RUN wget https://download.oracle.com/otn/linux/oracle18c/xe/oracle-database-xe-18c-1.0-1.x86_64.rpm.gz && gunzip oracle-database-xe-18c-1.0-1.x86_64.rpm.gz
# Copy RPM package to /tmp directory
COPY oracle-database-xe-18c-1.0-1.x86_64.rpm /tmp

# Install Oracle Database Express Edition (XE) Release 18.4.0.0.0 (18c)
RUN rpm -i /tmp/oracle-database-xe-18c-1.0-1.x86_64.rpm

# Set environment variables
ENV ORACLE_BASE=/opt/oracle
ENV ORACLE_HOME=/opt/oracle/product/18c/dbhomeXE
ENV ORACLE_SID=XE

# Create a symbolic link for the Oracle database binaries
RUN ln -s $ORACLE_HOME/bin $ORACLE_HOME/product/18c/dbhomeXE/bin

# Expose the Oracle database listener port
EXPOSE 1521

# Start the Oracle database listener
CMD ["/opt/oracle/product/18c/dbhomeXE/bin/lsnrctl", "start"]
