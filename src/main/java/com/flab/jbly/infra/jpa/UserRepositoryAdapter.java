package com.flab.jbly.infra.jpa;

import com.flab.jbly.domain.user.User;
import com.flab.jbly.domain.user.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

@Repository
@RequiredArgsConstructor
public class UserRepositoryAdapter implements UserRepository {

    private final UserJpaRepository repository;

    @Override
    public User save(User user) {
        return repository.save(user);
    }

    @Override
    public boolean existsByUserId(String userId) {
        return repository.existsByUserId(userId);
    }
}
