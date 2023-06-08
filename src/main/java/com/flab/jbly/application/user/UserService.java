package com.flab.jbly.application.user;

import com.flab.jbly.application.user.request.AccountDeleteServiceRequest;
import com.flab.jbly.application.user.request.AccountUpdateServiceRequest;
import com.flab.jbly.application.user.request.SignUpServiceRequest;
import com.flab.jbly.application.user.response.UserResponse;
import com.flab.jbly.domain.user.PasswordEncryption;
import com.flab.jbly.domain.user.User;
import com.flab.jbly.domain.user.UserRepository;
import com.flab.jbly.infrastructure.exception.ErrorCode;
import com.flab.jbly.infrastructure.exception.user.AccountMisMatchInfoException;
import com.flab.jbly.infrastructure.exception.user.DuplicatedUserException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@Transactional(readOnly = true)
public class UserService {

    private final UserRepository repository;
    private final PasswordEncryption passwordEncoder;

    public UserService(UserRepository repository, PasswordEncryption passwordEncoder) {
        this.repository = repository;
        this.passwordEncoder = passwordEncoder;
    }

    @Transactional
    public UserResponse saveUser(SignUpServiceRequest request) {
        if (repository.existsByUserId(request.getUserId())) {
            throw new DuplicatedUserException("DuplicatedUserException",
                ErrorCode.USER_DUPLICATION);
        }
        User newUser = User.builder()
            .userId(request.getUserId())
            .name(request.getName())
            .phone(request.getPhone())
            .email(request.getEmail())
            .address(request.getAddress())
            .password(passwordEncoder.encode(request.getPassword()))
            .build();
        repository.save(newUser);

        return new UserResponse(newUser.getUserId());
    }

    public UserResponse isUserExist(String userId) {
        if (repository.existsByUserId(userId)) {
            throw new DuplicatedUserException("DuplicatedUserException",
                ErrorCode.USER_DUPLICATION);
        }
        return new UserResponse(userId);
    }

    @Transactional
    public UserResponse deleteAccount(AccountDeleteServiceRequest command) {
        User user = repository.getUserById(command.Id());
        if (!user.getUserId().equals(command.userId())) {
            throw new AccountMisMatchInfoException("AccountMisMatchInfoException",
                ErrorCode.USER_INFO_MISMATCH);
        }
        repository.deleteUserById(user.getId());
        return new UserResponse(user.getUserId());
    }

    @Transactional
    public UserResponse update(AccountUpdateServiceRequest request) {
        User user = repository.getUserById(request.id());
        repository.save(user.update(
            request.userId(),
            passwordEncoder.encode(request.password()),
            request.name(),
            request.phone(),
            request.email(),
            request.address()
        ));
        return new UserResponse(user.getUserId());
    }

    @Transactional
    public void logout(){
    }
}
