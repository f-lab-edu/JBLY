package com.flab.jbly.domain.user;

public interface UserRepository {

		User findByUserId(String userId);

}
