package com.flab.jbly.infrastructure.auth;

import com.flab.jbly.domain.auth.Session;
import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;

public interface SessionJpaRepository extends JpaRepository<Session, Long> {

    Optional<Session> findBySessionToken(String sessionToken);
}
