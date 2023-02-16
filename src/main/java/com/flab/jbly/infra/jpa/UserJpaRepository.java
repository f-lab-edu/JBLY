package com.flab.jbly.infra.jpa;

import com.flab.jbly.domain.user.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserJpaRepository extends JpaRepository<User, Long> {

    boolean existsByUserId(String userId);

}
