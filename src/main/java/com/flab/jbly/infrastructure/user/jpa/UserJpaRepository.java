package com.flab.jbly.infrastructure.user.jpa;

import com.flab.jbly.domain.user.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserJpaRepository extends JpaRepository<User, Long> {

		User findByUserId(String userId);
}
