package com.flab.jbly.application.command;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import java.time.LocalDateTime;
import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@Builder
@AllArgsConstructor
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class UserSignUpCommand {

    @NotBlank(message = "아이디는 필수 입력 값입니다.")
    private String userId;

    @NotBlank(message = "비밀번호를 입력해주세요.")
    @Pattern(regexp = "(?=.*[0-9])(?=.*[a-zA-Z])(?=.*\\W)(?=\\S+$).{8,16}", message = "비밀번호는 8~16자 영문, 숫자, 특수문자를 사용하세요.")
    private String password;

    private String name;

    private String phone;

    private String email;

    private String address;

    private LocalDateTime createdAt;

    private LocalDateTime updatedAt;

}

