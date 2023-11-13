FROM jenkins/jenkins:latest
 
USER root
RUN apt-get update \
      && apt-get install -y sudo \
      && rm -rf /var/lib/apt/lists/*
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers
RUN sudo mkdir /var/jenkins_home/.ssh/
RUN ssh-keyscan -t rsa github.com >> known_hosts
 
USER jenkins
COPY plugins.txt /usr/share/jenkins/plugins.txt
#RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt
	