package com.flab.jbly.infrastructure.user.session;

import com.flab.jbly.domain.user.Session;
import org.springframework.data.jpa.repository.JpaRepository;

public interface SessionJpaRepository extends JpaRepository<Session, Long> {

}
