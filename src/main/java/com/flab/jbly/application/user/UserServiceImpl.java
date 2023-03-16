package com.flab.jbly.application.user;

import com.flab.jbly.application.user.command.AccountDeleteCommand;
import com.flab.jbly.application.user.command.AccountUpdateCommand;
import com.flab.jbly.application.user.command.UserSignUpCommand;
import com.flab.jbly.domain.user.PasswordEncryption;
import com.flab.jbly.domain.user.User;
import com.flab.jbly.domain.user.UserRepository;
import com.flab.jbly.infrastructure.exception.ErrorCode;
import com.flab.jbly.infrastructure.exception.user.AccountMisMatchInfoException;
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

    @Transactional(readOnly = true)
    public User getUserById(Long id) {
        return repository.getUserById(id);
    }

    @Transactional
    public void deleteAccount(AccountDeleteCommand command) {
        User user = repository.getUserById(command.Id());
        if (!user.getUserId().equals(command.userId())) {
            throw new AccountMisMatchInfoException("AccountMisMatchInfoException",
                ErrorCode.USER_INFO_MISMATCH);
        }
        repository.deleteUserById(user.getId());
    }

    @Transactional
    public void update(AccountUpdateCommand command) {
        User user = repository.getUserById(command.id());
        repository.save(user.update(
            command.userId(),
            passwordEncoder.encode(command.password()),
            command.name(),
            command.phone(),
            command.email(),
            command.address()
        ));
    }
}
