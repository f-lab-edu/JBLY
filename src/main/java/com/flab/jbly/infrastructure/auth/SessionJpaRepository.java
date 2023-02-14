package com.flab.jbly.infrastructure.auth;

import com.flab.jbly.domain.user.Session;
import org.springframework.data.jpa.repository.JpaRepository;

public interface SessionJpaRepository extends JpaRepository<Session, Long> {

}
