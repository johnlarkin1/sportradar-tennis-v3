from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_stream_statistics_event_id_item import GetStreamStatisticsEventIdItem
from ...models.get_stream_statistics_format import GetStreamStatisticsFormat
from ...models.get_stream_statistics_response_200_type_0 import GetStreamStatisticsResponse200Type0
from ...models.get_stream_statistics_response_200_type_1 import GetStreamStatisticsResponse200Type1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    format_: Union[Unset, GetStreamStatisticsFormat] = UNSET,
    event_id: Union[Unset, List[GetStreamStatisticsEventIdItem]] = UNSET,
    competition_id: Union[Unset, List[str]] = UNSET,
    season_id: Union[Unset, List[str]] = UNSET,
    sport_id: Union[Unset, List[str]] = UNSET,
    sport_event_id: Union[Unset, List[str]] = UNSET,
    format: str = "json",  # Added format parameter with default "json"
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    json_event_id: Union[Unset, List[str]] = UNSET
    if not isinstance(event_id, Unset):
        json_event_id = []
        for event_id_item_data in event_id:
            event_id_item = event_id_item_data.value
            json_event_id.append(event_id_item)

    params["event_id"] = json_event_id

    json_competition_id: Union[Unset, List[str]] = UNSET
    if not isinstance(competition_id, Unset):
        json_competition_id = competition_id

    params["competition_id"] = json_competition_id

    json_season_id: Union[Unset, List[str]] = UNSET
    if not isinstance(season_id, Unset):
        json_season_id = season_id

    params["season_id"] = json_season_id

    json_sport_id: Union[Unset, List[str]] = UNSET
    if not isinstance(sport_id, Unset):
        json_sport_id = sport_id

    params["sport_id"] = json_sport_id

    json_sport_event_id: Union[Unset, List[str]] = UNSET
    if not isinstance(sport_event_id, Unset):
        json_sport_event_id = sport_event_id

    params["sport_event_id"] = json_sport_event_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/stream/statistics/subscribe." + format,  # Append format directly if no path parameters
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["GetStreamStatisticsResponse200Type0", "GetStreamStatisticsResponse200Type1"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union["GetStreamStatisticsResponse200Type0", "GetStreamStatisticsResponse200Type1"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = GetStreamStatisticsResponse200Type0.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = GetStreamStatisticsResponse200Type1.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union["GetStreamStatisticsResponse200Type0", "GetStreamStatisticsResponse200Type1"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, GetStreamStatisticsFormat] = UNSET,
    event_id: Union[Unset, List[GetStreamStatisticsEventIdItem]] = UNSET,
    competition_id: Union[Unset, List[str]] = UNSET,
    season_id: Union[Unset, List[str]] = UNSET,
    sport_id: Union[Unset, List[str]] = UNSET,
    sport_event_id: Union[Unset, List[str]] = UNSET,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[Union["GetStreamStatisticsResponse200Type0", "GetStreamStatisticsResponse200Type1"]]:
    """Returns detailed, real-time information on every game statistics

    Args:
        format_ (Union[Unset, GetStreamStatisticsFormat]):
        event_id (Union[Unset, List[GetStreamStatisticsEventIdItem]]):
        competition_id (Union[Unset, List[str]]):
        season_id (Union[Unset, List[str]]):
        sport_id (Union[Unset, List[str]]):
        sport_event_id (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['GetStreamStatisticsResponse200Type0', 'GetStreamStatisticsResponse200Type1']]
    """

    kwargs = _get_kwargs(
        format_=format_,
        event_id=event_id,
        competition_id=competition_id,
        season_id=season_id,
        sport_id=sport_id,
        sport_event_id=sport_event_id,
        format=format,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, GetStreamStatisticsFormat] = UNSET,
    event_id: Union[Unset, List[GetStreamStatisticsEventIdItem]] = UNSET,
    competition_id: Union[Unset, List[str]] = UNSET,
    season_id: Union[Unset, List[str]] = UNSET,
    sport_id: Union[Unset, List[str]] = UNSET,
    sport_event_id: Union[Unset, List[str]] = UNSET,
    format: str = "json",  # Added format parameter to shorthand function as well
) -> Optional[Union["GetStreamStatisticsResponse200Type0", "GetStreamStatisticsResponse200Type1"]]:
    """Returns detailed, real-time information on every game statistics

    Args:
        format_ (Union[Unset, GetStreamStatisticsFormat]):
        event_id (Union[Unset, List[GetStreamStatisticsEventIdItem]]):
        competition_id (Union[Unset, List[str]]):
        season_id (Union[Unset, List[str]]):
        sport_id (Union[Unset, List[str]]):
        sport_event_id (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['GetStreamStatisticsResponse200Type0', 'GetStreamStatisticsResponse200Type1']
    """

    return sync_detailed(
        client=client,
        format_=format_,
        event_id=event_id,
        competition_id=competition_id,
        season_id=season_id,
        sport_id=sport_id,
        sport_event_id=sport_event_id,
        format=format,  # Pass format to sync_detailed
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, GetStreamStatisticsFormat] = UNSET,
    event_id: Union[Unset, List[GetStreamStatisticsEventIdItem]] = UNSET,
    competition_id: Union[Unset, List[str]] = UNSET,
    season_id: Union[Unset, List[str]] = UNSET,
    sport_id: Union[Unset, List[str]] = UNSET,
    sport_event_id: Union[Unset, List[str]] = UNSET,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[Union["GetStreamStatisticsResponse200Type0", "GetStreamStatisticsResponse200Type1"]]:
    """Returns detailed, real-time information on every game statistics

    Args:
        format_ (Union[Unset, GetStreamStatisticsFormat]):
        event_id (Union[Unset, List[GetStreamStatisticsEventIdItem]]):
        competition_id (Union[Unset, List[str]]):
        season_id (Union[Unset, List[str]]):
        sport_id (Union[Unset, List[str]]):
        sport_event_id (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['GetStreamStatisticsResponse200Type0', 'GetStreamStatisticsResponse200Type1']]
    """

    kwargs = _get_kwargs(
        format_=format_,
        event_id=event_id,
        competition_id=competition_id,
        season_id=season_id,
        sport_id=sport_id,
        sport_event_id=sport_event_id,
        format=format,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, GetStreamStatisticsFormat] = UNSET,
    event_id: Union[Unset, List[GetStreamStatisticsEventIdItem]] = UNSET,
    competition_id: Union[Unset, List[str]] = UNSET,
    season_id: Union[Unset, List[str]] = UNSET,
    sport_id: Union[Unset, List[str]] = UNSET,
    sport_event_id: Union[Unset, List[str]] = UNSET,
    format: str = "json",  # Added format parameter to async shorthand function
) -> Optional[Union["GetStreamStatisticsResponse200Type0", "GetStreamStatisticsResponse200Type1"]]:
    """Returns detailed, real-time information on every game statistics

    Args:
        format_ (Union[Unset, GetStreamStatisticsFormat]):
        event_id (Union[Unset, List[GetStreamStatisticsEventIdItem]]):
        competition_id (Union[Unset, List[str]]):
        season_id (Union[Unset, List[str]]):
        sport_id (Union[Unset, List[str]]):
        sport_event_id (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['GetStreamStatisticsResponse200Type0', 'GetStreamStatisticsResponse200Type1']
    """

    return (
        await asyncio_detailed(
            client=client,
            format_=format_,
            event_id=event_id,
            competition_id=competition_id,
            season_id=season_id,
            sport_id=sport_id,
            sport_event_id=sport_event_id,
            format=format,  # Pass format to asyncio_detailed
        )
    ).parsed
