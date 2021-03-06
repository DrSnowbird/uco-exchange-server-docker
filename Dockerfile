ARG BASE=${BASE:-openkbs/python-nonroot-docker}
FROM ${BASE}

MAINTAINER DrSnowbird "DrSnowbird@openkbs.org"

###############################
#### ---- App: (ENV)  ---- ####
###############################
USER ${USER:-developer}
WORKDIR ${HOME:-/home/developer}

ENV APP_HOME=${APP_HOME:-$HOME/app}
ENV APP_MAIN=${APP_MAIN:-setup.sh}

#################################
#### ---- App: (common) ---- ####
################################
WORKDIR ${APP_HOME}
RUN python -u -m pip install --upgrade pip

###############################
#### ---- App Setup:  ---- ####
###############################
COPY --chown=$USER:$USER ./app $HOME/app
COPY --chown=$USER:$USER ./bin $HOME/bin
RUN $HOME/bin/pre-load-virtualenv.sh && \
    if [ -s $HOME/app/requirements.txt ]; then \
        pip install --no-cache-dir -r requirements.txt ; \
        pip install connexion[swagger-ui]; \
    fi; 
    
#########################################
##### ---- Setup: Entry Files  ---- #####
#########################################
COPY --chown=${USER}:${USER} docker-entrypoint.sh /
COPY --chown=${USER}:${USER} ${APP_MAIN} ${APP_HOME}/setup.sh
RUN sudo chmod +x /docker-entrypoint.sh ${APP_HOME}/setup.sh 

#########################################
##### ---- Docker Entrypoint : ---- #####
#########################################
ENTRYPOINT ["/docker-entrypoint.sh"]

#####################################
##### ---- user: developer ---- #####
#####################################
WORKDIR ${APP_HOME}
USER ${USER}

#############################################
#############################################
#### ---- App: (Customization here) ---- ####
#############################################
#############################################
#RUN pip install --user connexion[swagger-ui]

######################
#### (Test only) #####
######################
#CMD ["/bin/bash"]
######################
#### (RUN setup) #####
######################
CMD ["setup.sh"]

#ENTRYPOINT ["python"]
#CMD ["-m", "swagger_server"]

