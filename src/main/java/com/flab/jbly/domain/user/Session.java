package com.flab.jbly.domain.user;


import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;
import lombok.AccessLevel;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "session")
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Session {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "session_id")
    private Long id;

    @Column(name = "user_id")
    @NotNull
    private Long userId;

    @Column(name = "session_info")
    private String sessionInfo;

    private Session(Long userId, String sessionInfo) {
        this.userId = userId;
        this.sessionInfo = sessionInfo;
    }

    public static Session of(Long userId, String sessionInfo) {
        return new Session(userId, sessionInfo);
    }
}
