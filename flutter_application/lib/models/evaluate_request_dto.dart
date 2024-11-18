import 'package:json_annotation/json_annotation.dart';

part 'evaluate_request_dto.g.dart';

@JsonSerializable()
class EvaluateRequestDto {
  String image;

  EvaluateRequestDto({
    required this.image,
  });

  factory EvaluateRequestDto.fromJson(Map<String, dynamic> json) =>
      _$EvaluateRequestDtoFromJson(json);

  Map<String, dynamic> toJson() => _$EvaluateRequestDtoToJson(this);
}
