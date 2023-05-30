package com.flab.jbly.domain.user;

import com.flab.jbly.domain.common.BaseEntity;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Entity
@AllArgsConstructor
@Builder
@Getter
@Table(name = "users")
public class User extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "userId", nullable = false, length = 100)
    private String userId;

    @Column(nullable = false, length = 500)
    private String password;

    @Column(nullable = false, length = 100)
    private String name;

    @Column(nullable = false)
    private String phone;

    @Column(nullable = false)
    private String email;

    @Column(nullable = false)
    private String address;

    // Test 시에만 사용됩니다.
    public void currentId(Long id) {
        this.id = id;
    }

    // Update User Info
    public User update(String userId, String pw, String name, String phone, String email, String address) {
        this.userId = userId;
        this.password = pw;
        this.name = name;
        this.phone = phone;
        this.email = email;
        this.address = address;
        return this;
    }
}
