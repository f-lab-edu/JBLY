package com.flab.jbly.infrastructure.user.exception;

public class UserPasswordNotMatchedException extends IllegalArgumentException {

		public UserPasswordNotMatchedException() {
		}

		public UserPasswordNotMatchedException(String s) {
				super(s);
		}
}
