package com.flab.jbly.domain.user;

import java.time.LocalDateTime;
import lombok.AccessLevel;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class User {

		private Long id;

		private String userId;

		private String password;

		private String name;

		private String phone;

		private String email;

		private String address;

		private LocalDateTime createdAt;

		private LocalDateTime updatedAt;
}

