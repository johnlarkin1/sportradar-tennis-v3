from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sport_event_timeline_locale import GetSportEventTimelineLocale
from ...models.get_sport_event_timeline_response_200 import GetSportEventTimelineResponse200
from ...types import Response


def _get_kwargs(
    locale: GetSportEventTimelineLocale,
    urn_sport_event: str,
    format: str = "json",  # Added format parameter with default "json"
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/sport_events/{urn_sport_event}/timeline" + f".{format}",  # Append format to URL
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetSportEventTimelineResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetSportEventTimelineResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetSportEventTimelineResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetSportEventTimelineLocale,
    urn_sport_event: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetSportEventTimelineResponse200]:
    """show summary and timeline for one sport event

     Show a summary and timeline for one sport event, including results.

    Args:
        locale (GetSportEventTimelineLocale):
        urn_sport_event (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSportEventTimelineResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_sport_event=urn_sport_event, format=format)

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: GetSportEventTimelineLocale,
    urn_sport_event: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to shorthand function as well
) -> Optional[GetSportEventTimelineResponse200]:
    """show summary and timeline for one sport event

     Show a summary and timeline for one sport event, including results.

    Args:
        locale (GetSportEventTimelineLocale):
        urn_sport_event (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSportEventTimelineResponse200
    """

    return sync_detailed(
        locale=locale,
        urn_sport_event=urn_sport_event,
        client=client,
        format=format,  # Pass format to sync_detailed
    ).parsed


async def asyncio_detailed(
    locale: GetSportEventTimelineLocale,
    urn_sport_event: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetSportEventTimelineResponse200]:
    """show summary and timeline for one sport event

     Show a summary and timeline for one sport event, including results.

    Args:
        locale (GetSportEventTimelineLocale):
        urn_sport_event (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSportEventTimelineResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_sport_event=urn_sport_event, format=format)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: GetSportEventTimelineLocale,
    urn_sport_event: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to async shorthand function
) -> Optional[GetSportEventTimelineResponse200]:
    """show summary and timeline for one sport event

     Show a summary and timeline for one sport event, including results.

    Args:
        locale (GetSportEventTimelineLocale):
        urn_sport_event (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSportEventTimelineResponse200
    """

    return (
        await asyncio_detailed(
            locale=locale,
            urn_sport_event=urn_sport_event,
            client=client,
            format=format,  # Pass format to asyncio_detailed
        )
    ).parsed
