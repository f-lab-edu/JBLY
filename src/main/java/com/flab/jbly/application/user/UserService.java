package com.flab.jbly.application.user;

import com.flab.jbly.application.user.command.UserSignUpCommand;
import org.springframework.stereotype.Service;

@Service
public interface UserService {

    void saveUser(UserSignUpCommand command);

    boolean isUserExist(String userId);

}
