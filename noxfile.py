import nox

nox.options.reuse_existing_virtualenvs = True

build_command = ["-b", "html", "docs/source", "docs/build/html"]

@nox.session(python="3.11")
def docs(session):
    session.install("-r", "docs/doc-requirements.txt")
    session.run("sphinx-build", *build_command)

@nox.session(name="docs-live", python="3.11")
def docs_live(session):
    session.install("-r", "docs/doc-requirements.txt")
    session.install("sphinx-autobuild")

    AUTOBUILD_IGNORE = [
        "docs/build",
    ]
    cmd = ["sphinx-autobuild"]
    for folder in AUTOBUILD_IGNORE:
        cmd.extend(["--ignore", f"*/{folder}/*"])
    cmd.extend(build_command)
    session.run(*cmd)
