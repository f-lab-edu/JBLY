package com.flab.jbly.application.user;

import com.flab.jbly.domain.user.PasswordEncryption;
import com.flab.jbly.domain.user.User;
import com.flab.jbly.domain.user.UserRepository;
import com.flab.jbly.application.user.command.UserSignUpCommand;
import com.flab.jbly.infrastructure.exception.ErrorCode;
import com.flab.jbly.infrastructure.exception.user.DuplicatedUserException;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

    private final UserRepository repository;
    private final PasswordEncryption passwordEncoder;

    @Transactional
    public void saveUser(UserSignUpCommand command) {
        if (isUserExist(command.getUserId())) {
            throw new DuplicatedUserException("DuplicatedUserException",
                ErrorCode.USER_DUPLICATION);
        }
        User newUser = User.builder()
            .userId(command.getUserId())
            .name(command.getName())
            .phone(command.getPhone())
            .email(command.getEmail())
            .address(command.getAddress())
            .password(passwordEncoder.encode(command.getPassword()))
            .build();
        repository.save(newUser);
    }

    @Transactional(readOnly = true)
    public boolean isUserExist(String userId) {
        if (repository.existsByUserId(userId)) {
            throw new DuplicatedUserException("DuplicatedUserException",
                ErrorCode.USER_DUPLICATION);
        }
        return false;
    }

    public User getUserById(Long id) {
        return repository.getUserById(id);
    }
}
