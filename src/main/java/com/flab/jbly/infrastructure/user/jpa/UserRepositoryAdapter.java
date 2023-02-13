package com.flab.jbly.infrastructure.user.jpa;

import com.flab.jbly.domain.user.User;
import com.flab.jbly.domain.user.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

@Repository
@RequiredArgsConstructor
public class UserRepositoryAdapter implements UserRepository {

		private final UserJpaRepository repository;

		@Override
		public User findByUserId(String userId) {
				return repository.findByUserId(userId);
		}
}
