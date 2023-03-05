package com.flab.jbly.infrastructure.jpa.user;

import com.flab.jbly.domain.user.User;
import com.flab.jbly.domain.user.UserRepository;
import com.flab.jbly.infrastructure.exception.ErrorCode;
import com.flab.jbly.infrastructure.exception.user.DoesNotExistUserException;
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

    @Override
    public User save(User user) {
        return repository.save(user);
    }

    @Override
    public boolean existsByUserId(String userId) {
        return repository.existsByUserId(userId);
    }

    @Override
    public User getUserById(Long id) {
        return repository.findById(id).orElseThrow(
            () -> new DoesNotExistUserException("DoesNotExistUserException",
                ErrorCode.USER_DOES_NOT_EXIST));
    }
}
