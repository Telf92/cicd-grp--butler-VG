FROM jenkins/jenkins:lts
USER root
RUN apt-get update && apt-get install -y apt-transport-https \
    ca-certificates curl gnupg2 \
    software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) stable"
RUN apt-get update && apt-get install -y docker-ce-cli jq
RUN apt-get install -y python3 python3-pip python3-venv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install black pylint pytest

#Jenkins plugins for the image:
RUN jenkins-plugin-cli --plugins "warnings-ng" && \
    jenkins-plugin-cli --plugins "branch-api" && \
    jenkins-plugin-cli --plugins "snakeyaml-api" && \
    jenkins-plugin-cli --plugins "bootstrap5-api" && \
    jenkins-plugin-cli --plugins "pam-auth" && \
    jenkins-plugin-cli --plugins "echarts-api" && \
    jenkins-plugin-cli --plugins "instance-identity" && \
    jenkins-plugin-cli --plugins "pipeline-graph-analysis" && \
    jenkins-plugin-cli --plugins "gradle" && \
    jenkins-plugin-cli --plugins "matrix-auth" && \
    jenkins-plugin-cli --plugins "matrix-project" && \
    jenkins-plugin-cli --plugins "prism-api" && \
    jenkins-plugin-cli --plugins "workflow-aggregator" && \
    jenkins-plugin-cli --plugins "pipeline-groovy-lib" && \
    jenkins-plugin-cli --plugins "jquery3-api" && \
    jenkins-plugin-cli --plugins "plugin-util-api" && \
    jenkins-plugin-cli --plugins "javax-activation-api" && \
    jenkins-plugin-cli --plugins "font-awesome-api" && \
    jenkins-plugin-cli --plugins "pipeline-model-api" && \
    jenkins-plugin-cli --plugins "github-branch-source" && \
    jenkins-plugin-cli --plugins "github" && \
    jenkins-plugin-cli --plugins "workflow-support" && \
    jenkins-plugin-cli --plugins "checks-api" && \
    jenkins-plugin-cli --plugins "workflow-job" && \
    jenkins-plugin-cli --plugins "caffeine-api" && \
    jenkins-plugin-cli --plugins "okhttp-api" && \
    jenkins-plugin-cli --plugins "ssh-credentials" && \
    jenkins-plugin-cli --plugins "analysis-model-api" && \
    jenkins-plugin-cli --plugins "jjwt-api" && \
    jenkins-plugin-cli --plugins "pipeline-model-definition" && \
    jenkins-plugin-cli --plugins "workflow-multibranch" && \
    jenkins-plugin-cli --plugins "mina-sshd-api-common" && \
    jenkins-plugin-cli --plugins "mailer" && \
    jenkins-plugin-cli --plugins "pipeline-stage-step" && \
    jenkins-plugin-cli --plugins "ssh-slaves" && \
    jenkins-plugin-cli --plugins "jaxb" && \
    jenkins-plugin-cli --plugins "ldap" && \
    jenkins-plugin-cli --plugins "pipeline-stage-tags-metadata" && \
    jenkins-plugin-cli --plugins "forensics-api" && \
    jenkins-plugin-cli --plugins "plain-credentials" && \
    jenkins-plugin-cli --plugins "script-security" && \
    jenkins-plugin-cli --plugins "git-client" && \
    jenkins-plugin-cli --plugins "pipeline-input-step" && \
    jenkins-plugin-cli --plugins "mina-sshd-api-core" && \
    jenkins-plugin-cli --plugins "build-timeout" && \
    jenkins-plugin-cli --plugins "commons-text-api" && \
    jenkins-plugin-cli --plugins "workflow-durable-task-step" && \
    jenkins-plugin-cli --plugins "token-macro" && \
    jenkins-plugin-cli --plugins "pipeline-model-extensions" && \
    jenkins-plugin-cli --plugins "javax-mail-api" && \
    jenkins-plugin-cli --plugins "credentials-binding" && \
    jenkins-plugin-cli --plugins "git" && \
    jenkins-plugin-cli --plugins "workflow-basic-steps" && \
    jenkins-plugin-cli --plugins "resource-disposer" && \
    jenkins-plugin-cli --plugins "jakarta-activation-api" && \
    jenkins-plugin-cli --plugins "github-api" && \
    jenkins-plugin-cli --plugins "trilead-api" && \
    jenkins-plugin-cli --plugins "workflow-cps" && \
    jenkins-plugin-cli --plugins "timestamper" && \
    jenkins-plugin-cli --plugins "workflow-api" && \
    jenkins-plugin-cli --plugins "cloudbees-folder" && \
    jenkins-plugin-cli --plugins "structs" && \
    jenkins-plugin-cli --plugins "jakarta-mail-api" && \
    jenkins-plugin-cli --plugins "apache-httpcomponents-client-4-api" && \
    jenkins-plugin-cli --plugins "data-tables-api" && \
    jenkins-plugin-cli --plugins "pipeline-milestone-step" && \
    jenkins-plugin-cli --plugins "jackson2-api" && \
    jenkins-plugin-cli --plugins "variant" && \
    jenkins-plugin-cli --plugins "pipeline-build-step" && \
    jenkins-plugin-cli --plugins "pipeline-rest-api" && \
    jenkins-plugin-cli --plugins "scm-api" && \
    jenkins-plugin-cli --plugins "display-url-api" && \
    jenkins-plugin-cli --plugins "durable-task" && \
    jenkins-plugin-cli --plugins "pipeline-github-lib" && \
    jenkins-plugin-cli --plugins "workflow-step-api" && \
    jenkins-plugin-cli --plugins "credentials" && \
    jenkins-plugin-cli --plugins "ant" && \
    jenkins-plugin-cli --plugins "pipeline-stage-view" && \
    jenkins-plugin-cli --plugins "bouncycastle-api" && \
    jenkins-plugin-cli --plugins "junit" && \
    jenkins-plugin-cli --plugins "commons-lang3-api" && \
    jenkins-plugin-cli --plugins "workflow-scm-step" && \
    jenkins-plugin-cli --plugins "ws-cleanup" && \
    jenkins-plugin-cli --plugins "antisamy-markup-formatter" && \
    jenkins-plugin-cli --plugins "ionicons-api" && \
    jenkins-plugin-cli --plugins "email-ext"

RUN groupadd docker || true
RUN usermod -aG docker jenkins

USER jenkins
