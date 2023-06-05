name = "glm"

authors = [
    "OpenGL Mathematics"
]

# NOTE: version = <external_version>.sse.<sse_version>
version = "0.9.9.8.sse.1.0.0"

description = """OpenGL Mathematics"""

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]
    #c.build_thread_count = "physical_cores"

requires = [
]

private_build_requires = [
]

variants = [
]

uuid = "repository.glm"
build_command = "rez python {root}/rez_build.py"


def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    # NOTE: REZ package versions can have ".sse." to separate the external
    # version from the internal modification version.
    split_versions = str(version).split(".sse.")
    external_version = split_versions[0]
    internal_version = None
    if len(split_versions) == 2:
        internal_version = split_versions[1]

    env.GLM_VERSION = external_version
    env.GLM_PACKAGE_VERSION = external_version
    if internal_version:
        env.GLM_PACKAGE_VERSION = internal_version

    env.GLM_ROOT.append("{root}")
    env.GLM_LOCATION.append("{root}")

def post_commands():
    pass
