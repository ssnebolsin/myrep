
import msal
import auth_config
import logging

from flask import url_for, session


def build_msal_app(cache=None, authority=None):
    return msal.ConfidentialClientApplication(
        auth_config.CLIENT_ID, authority=authority or auth_config.AUTHORITY,
        client_credential=auth_config.CLIENT_SECRET, token_cache=cache)


def build_auth_code_flow(authority=None, scopes=None):
    scheme = "https" if url_for("authorized", _external=True) != "http://localhost:5000/auth" else "http"
    logging.warning("scheme={}".format(scheme))
    logging.warning("redirect_uri={}".format(url_for("authorized", _external=True, _scheme=scheme)))
    print(scheme)
    print(url_for("authorized", _external=True, _scheme=scheme))
    return build_msal_app(authority=authority).initiate_auth_code_flow(
        scopes or [],
        redirect_uri=url_for("authorized", _external=True, _scheme=scheme))


def load_auth_cache():
    cache = msal.SerializableTokenCache()
    if session.get("token_cache"):
        cache.deserialize(session["token_cache"])
    return cache


def save_auth_cache(cache):
    if cache.has_state_changed:
        session["token_cache"] = cache.serialize()
