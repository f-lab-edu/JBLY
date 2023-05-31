package com.flab.jbly.domain.user;

public interface UserRepository {

    User save(User user);

    boolean existsByUserId(String userId);

    User findByUserId(String userId);

    User getUserById(Long id);

    void deleteUserById(Long id);

    void deleteAllInBatch();
}
