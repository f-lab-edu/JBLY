package com.flab.jbly.domain.user;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;
import java.time.Instant;
import lombok.AccessLevel;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Entity
@Table(name = "user")
public class User {

		@Id
		@GeneratedValue(strategy = GenerationType.IDENTITY)
		@Column(name = "id")
		private Long id;

		@NotNull
		@Column(name = "userId")
		private String userId;

		@NotNull
		private String password;

		private String name;

		private String phone;

		private String email;

		private String address;

		@CreationTimestamp
		@Column(name = "created_at")
		@NotNull
		private Instant createdAt;

		@UpdateTimestamp
		@Column(name = "updated_at")
		private Instant updatedAt;
}

