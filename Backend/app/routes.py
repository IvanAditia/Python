from flask import Blueprint, Request

auth = Blueprint('auth', __name__)

@auth.route("/", methods=['GET', 'POST'])
def main():
  return 