package com.flab.jbly.application.user;

import com.flab.jbly.application.user.command.AccountDeleteCommand;
import com.flab.jbly.application.user.command.UserSignUpCommand;
import com.flab.jbly.domain.user.User;
import org.springframework.stereotype.Service;

@Service
public interface UserService {

    void saveUser(UserSignUpCommand command);

    boolean isUserExist(String userId);

    User getUserById(Long id);

    void deleteUserAccount(AccountDeleteCommand command);

}
