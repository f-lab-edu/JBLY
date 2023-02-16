package com.flab.jbly.application.service;

import com.flab.jbly.application.command.UserSignUpCommand;
import org.springframework.stereotype.Service;

@Service
public interface UserService {

    void saveUser(UserSignUpCommand command);

    boolean isUserExist(String userId);

}
