# Python 3.9
FROM public.ecr.aws/docker/library/python:3.9-slim-buster

########################################################
# LINUX PACKAGES
########################################################
RUN apt-get update && apt-get install -y \
        zip \
        g++ \
        gcc \
        make \
        cmake \
        autoconf \
        automake \
        unzip \
        perl \
        git \
        wget \
        libssl-dev \
        libncurses5-dev \
        zlib1g-dev \
        libxslt-dev \
        libxml2-dev \
        zlib1g-dev \
        liblzma-dev \
        libbz2-dev \
        gawk \
        && rm -rf /var/lib/apt/lists/* \
        && apt-cache search linux-headers-generic

RUN apt-get update


ARG FUNCTION_DIR="/function"

# Copy function code
RUN mkdir -p ${FUNCTION_DIR}

# Update pip
ARG LITHOPS


########################################################
# PYTHON MODULES
########################################################
RUN pip install --upgrade --ignore-installed pip wheel six setuptools \
    && pip install --upgrade --no-cache-dir --ignore-installed \
	awslambdaric \
        httplib2 \
        requests \
        numpy \
        scipy \
        pandas \
        pika \
        kafka-python \
        cloudpickle \
        ps-mem \
        tblib \
        tenacity \
        psutil \
        ipykernel \
        ipywidgets \
        ipyleaflet \
        botocore==1.29.76 \
        boto3==1.26.76 \
        redis \
        matplotlib \
        donfig \
        toolz \
        array-api-compat \
        networkx \
        mypy_extensions \
        zarr \
        ndindex \
        seaborn \
        aiostream

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip six wheel setuptools && \
   pip install --no-cache-dir --no-dependencies -r requirements.txt


# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

#ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
#CMD [ "handler.entry_point.lambda_handler" ]