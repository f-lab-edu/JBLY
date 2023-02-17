package com.flab.jbly.infrastructure.exception;

public class UserPasswordNotMatchedException extends IllegalArgumentException {

		public UserPasswordNotMatchedException() {
		}

		public UserPasswordNotMatchedException(String s) {
				super(s);
		}
}
