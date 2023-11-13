FROM jenkins/jenkins:lts
USER root
RUN apt-get update && apt-get install -y apt-transport-https \
    ca-certificates curl gnupg2 \
    software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) stable"
RUN apt-get update && apt-get install -y docker-ce-cli
RUN apt-get install -y python3
RUN groupadd docker || true
RUN usermod -aG docker jenkins
RUN mkdir /var/jenkins_home/.ssh/
RUN ssh-keyscan -t rsa github.com >> /var/jenkins_home/.ssh/known_hosts
USER jenkins
