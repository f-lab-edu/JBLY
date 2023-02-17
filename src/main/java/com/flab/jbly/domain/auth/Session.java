package com.flab.jbly.domain.auth;


import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;
import java.io.Serializable;
import lombok.AccessLevel;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "session")
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Session implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "session_id")
    private Long id;

    @Column(name = "user_id")
    @NotNull
    private Long userId;

    @Column(name = "session_token")
    private String sessionToken;

    private Session(Long userId, String sessionToken) {
        this.userId = userId;
        this.sessionToken = sessionToken;
    }

    public static Session of(Long userId, String sessionToken) {
        return new Session(userId, sessionToken);
    }
}
